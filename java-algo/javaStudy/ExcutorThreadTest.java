/**
 * ExcutorThreadTest
 */
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;

public class ExcutorThreadTest {

    public static void main(String[] args) {
        // ThreadPoolExcutor를 사용해서, ThreadPool을 만들 수 있게 됨.
        // Excutors의 newFixedQueue 같은 경우, 고정된 풀 사이즈를 만들긴 하지만, 
        // Unbounded Queue기 때문에, 기본적으로 Integer.MAX_VALUE를 가지고 있기 때문에
        // 20억개의 Task가 큐에 들어오게 됨.
        // Thread개수를 20억개로 설정할 수 없기 때문에, 20억개의 요청이 밀려 들어온다는 것은
        // 메모리를 많이 잡아 먹게 된다는 것.
        // 그러므로, Unbounded Queue를 사용하기 보다. BoundedQueue를 사용하는게 바람직함.
        

        // 그러나 newFixed 정적 메소드인 경우, Argument를 직접 넘길 수 없기 때문에
        // QueueSize를 특정할 수 없음. 그러므로 새로운 BlockingQueue를 넘겨 주어야 함.
        // 그래서 ArrayBlockQueue를 보낼 수 있음.
        // ArrayBlockQueue르 보내면서, Queue의 size를 특정할 수 있게됨.
        // 그러나, Queue의 Size를 특정 했다고 하더라도, Queue size만큼만 Queue요청을 받도록
        // 바운더리를 쳐준것 뿐이지. 그 외 externel task에 대한 처리 부분은 workQueue가 처리해줄 수 없음.


        // 그렇기 때문에 ThreadPoolExecutor 생성자의 Argument로, rejectHandler를 같이 넘겨주어야 함.
        // 그렇다면, 외부 external task에 대한 처리를 할 수 있게 됨.


        // RejectedExecutorHandler를 전달하게 되고,
        // JavaAPI에서, 이러한 external task에 대한 핸들러인 리젝 핸들러를 제공해준다.
        // ThreadPoolExcutor.AbortPolicy는 항상 thrwo RejectException을 반환한다.


        // ThreadPoolExcutor의 CallerRunsPolicy를 사용하게 되면, rejected된 task를 실행할 수 있도록 해준다.

        // CallerRunPolicy class의 instance를 만들어서, shutdown되는게 아니라면 rejected task를 실행한다.
        // 만약 shutdown이 된다면, discard되어진다.


        // 몇가지 rejectedTask를 다룰 수 있는, Policy 클래스를 내부 클래스로 제공해준다.
        // rejectExcution을 caller's thread가 실행하게 되는 것.
        // 그럼 shutdown된게 아니라면 run() 해당 task Runnable의 task를 실행하게 된다.
        ExcutorService excutorService = new ThreadPoolExecutor(
            0, 
            0, 
            0, 
            null, 
            null, 
            new ThreadPoolExecutor.CallerRunsPolicy());



    }

    // java의 blocking queue는 Thread Safe하다.
    // 모든 메소드가 동시성을 컨트롤 한다.
    // Thread Safe 하다는건 race condition이 발생할 여지를 동기화로 인해
    // 해결해준다는 것을 의미한다.
    
}