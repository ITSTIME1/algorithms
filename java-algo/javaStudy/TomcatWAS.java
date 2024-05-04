
import java.net.ServerSocket;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;
import java.util.logging.Logger;
import java.util.stream.IntStream;

/**
 * TomcatWAS 구축기.
 */
public class TomcatWAS {
    // for storing log
    // private static final Logger logger = LoggerFactory.getLogger(TomcatWAS.class);

    // default server port for server role
    private static final int DEFAULT_PORT = 8080;

    /*
     * specified thread pool size. 
     * 
     * this static variable is for maximum thread count. 
     */
    
    private static final int DEFAULT_THREAD_POOL_SIZE = 250;

    /**
     * specified blocking queue size.
     * 
     * if thread was reached to @DEFAULT_THREAD_POOL_SiZE that can wait until thread available.
     * so, purpose of queue is stored tasks.
     * but, we must limit size for queue. this is bounded queue.
     * 
     * if you implemenet unbounded queue, thread pool instance applys Integer.MAXINTEGER (two billions.)
     * 
     * hence, you must specify limited queue size. 
     * 
     */

    private static final int DEFAULT_THREAD_QUEUE_SIZE = 100;   

    
    private static ThreadPoolExecutor threadPoolExcutor(int corePoolSize, int queueSize) {
        return new ThreadPoolExecutor(corePoolSize, corePoolSize, queueSize, TimeUnit.MILLISECONDS, new LinkedBlockingQueue<>());
    }

    /*
     * 총 Thread 개수보다 적은 동시 요청을 보냈을때 WAS가 정상 동작하는지 검증하는 테스트 코드.
     * 총 Thread 개수보다 적은 요청을 보낸다는 것은, Thread를 전부 사용하지 않게 되고, 유휴상태(idle)상태의 쓰레드들이 존재한다는 것.
     * 그러므로, coreThreadSize보다 적은 동시요청을 처리할 수 있음.
     * 
     * expected 값은 WAS가 정상적으로 작동하길 기대할 수 있음.
     * -> Thread수는 곧 작업의 최소 처리단위라고 생각해보면, 처리할 수 있는 작업의 개수를 넘어가지 않으므로
     * WAS에서 메모리문제가 발생하지 않고, 모든 처리를 수행할 것으로 예상이 가능.
     * 
     */
    void requestUnderMaxThreadSize() throws InterruptedException{
        /**
         * @param : {threadPoolSize} is total thread size.
         * @param : {requestCount} is total request size.
         * 
         * If thread was successful task requestCount decrease.
         * 
         * thread size bigger than requestCount, I was expected to success all tasks.
         * 
         * CountDownLatch 는 어떤 쓰레드의 작업이 끝날때까지 기다리게 해준다.
         * 즉 일정 개수의 쓰레드가 모두 끝날 때 까지 기다려야지만 다음으로 진행할 수 있거나, 다른 쓰레드를 실행시킬 수 있는 경우.
         * 
         * 예를들어, 각 작업을 병렬로 처리한 다음에, batch process를 진행할 필요가 있을때, 사용한다.
         * 병렬로 처리한 결과를 데이터베이스에 일괄로 처리해야 한다면, batch process를 진행할 필요가 있고
         * 이 배치 프로세스를 위해서, 이전 thread들의 병렬처리가 선행되어야지, 수행이 가능하다.
         * 수행한 결과만 일괄로 처리할 수 있게 해주는 클래스가 바로 CountDownLatch다.
         * 
         * 그럼 CountDownLatch가 어떻게 동작하는가?
         * CountdownLatch 인스턴스를 만들어서 동작하면, 초기에 설정해 두었던 int tpye의 count로 초기화가 된다.
         * 그러면 thread들이 자신의 작업이 끝났음을 알리기 위해서, countDown()메소드로 알려준다.
         * 즉 count를 하나씩 소비하는것을 의미한다.
         * 
         * 이제 이 쓰레드들이 끝나기를 기다리는 쪽에서는 await()메소드를 호출해서 모든 쓰레드들이 끝나기를 기다린다.
         * 
         * 
         */
        final int threadPoolSize = 200;
        int requestCount = 100;

        CountDownLatch countDownLatch = new CountDownLatch(requestCount);
        IntStream.range(0, requestCount).parallel().forEach(n -> excutorService.excute() -> {
            RestTemplate restTemplate = new RestTemplate();
            // 특정 get 요청을 한다.
            ResponseEntity<String> response = restTemplate.getForEntity();
            // 이런식으로, thread들이 작업을 n번만큼 수행하게 될때, 마지막에
            // 각 Thread가 coundDown() 메소드를 호출함으로써, latch 횟수를 줄인다.
            // 그러면 각 thread의 잔여량을 파악할 수 있다.
            // 다만 spring boot에서는 직접 thread pool을 구현하지 않는다.
            // properties 파일에 thread설정을 미리 하고 관리하기 때문이다.

            countDownLatch.countDown();
            

        });
        // awiat메소드를 호출해서, 모든 쓰레드들이 끝날때까지 기다려준다.
        // 즉 이때는 mainThread입장에서 기다려주어야 한다는것.
        boolean await = countDownLatch.await();


    }
    public static void main(String[] args) {

        /**
         * Java API provides ThreadPoolExcutor from java.util.concurrent pacakage.
         * ThreadPoolExecutor can implement thread pool.
         * 
         * first, we will implement thread pool by using ThreadPoolExcutor. 
         * Internally that was implemented blokcing queue for stored tasks when all thread not available.
         * 
         * excute() method of threadPoolExcutor run 
         */
        // 이제 ThreadPoolExcutor를 반환받을건데, 
        // tomcat이 threadPoolExcutor를 가지고 있다고하ㅏㅈ.
        ThreadPoolExecutor threadPoolExecutor = threadPoolExcutor(DEFAULT_THREAD_POOL_SIZE, DEFAULT_THREAD_QUEUE_SIZE);
        
    }
}