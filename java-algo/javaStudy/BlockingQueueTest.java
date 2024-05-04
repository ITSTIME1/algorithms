/**
 * BlockingQueueTest
 */
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

class Message {
    private String msg = null;
    public Message(String i) 
    {
        msg = i;
    }
    public String getMsg() {
        return msg;
    }
    public void setMsg(String msg) {
        this.msg = msg;
    }
    
    
}

/**
 * Producer can support task, so msg task was inserted blocking queue by produce per minute.
 */
class Producer implements Runnable {

    // run method 강제 구현.
    private BlockingQueue<Message> queue;

    // factory 
    // this can't create BlockingQueue externel class.
    public Producer(BlockingQueue<Message> queue) {
        this.queue = queue;
        System.out.println("Producer = " + queue.hashCode());
    }
    @Override
    public void run() {
        for (int i = 0; i < 100; i++) {
            // Thread가 run()메소드를  실행할테니까
            Message msg = new Message(String.valueOf(i));
            try {
                Thread.sleep(i);
                queue.put(msg);
                System.out.println("Produced "+msg.getMsg());
            }catch(InterruptedException e ) {
                e.printStackTrace();
            }
        }

        // Last, 
        // if there is in queue, Consumer take tasks from blockingQueue
        // independent run each of thread
        // step by step, but randomly feature 
        Message msg = new Message("exit");
        try {
            queue.put(msg);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    
}

/**
 * Consumer class consume task from queue
 */
class Consumer implements Runnable{

        private BlockingQueue<Message> queue;
        
        public Consumer(BlockingQueue<Message> q){
            this.queue=q;
            System.out.println("Consumer = " + queue.hashCode());
        }
    
        @Override
        public void run() {
            try{
                Message msg;
                //consuming messages until exit message is received
                while((msg = queue.take()).getMsg() !="exit"){
                Thread.sleep(10);
                // this method consume
                System.out.println("Consumed "+ msg.getMsg());
                }
            }catch(InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    // 이런식으로 동작한다는 것을 보여주는거지.
    // 아 생각해보니까 참조니까 자바는, 같은 queue를 가리키겠지.
    // 
public class BlockingQueueTest {

    public static void main(String[] args) {
        // capacity = 10 is equal to queue max size = 10
        // That's mean meant ArrayBlockingQueue Bounded queue.
        // if queue has been shut down, discard task
        // but hasn't been shut down, not discard task. == run task
        BlockingQueue<Message> queue = new ArrayBlockingQueue<>(10);


        // why send queue object into Producer object?
        // Producer can make tasks so, needed queue for stored purpose.
        // and 
        Producer producer = new Producer(queue);
        Consumer consumer = new Consumer(queue);
        //starting producer to produce messages in queue
        // 어떻게 공유되냐면 자바의 객체전달은 참조타입임
        // 참조라고 한다면 실제 값이 저장되어 있는것을, alias를 가지고 있다는것.
        // 그래서 이 alias를 이용해서 접근을 하게 됨.
        // 생성자로 넘어온 queue를 확인해보면, queue의 hashCode값이 같은것을 확인할 수 있음.
        // 즉 같은 hashCode를 갖고 있기 때문에
        // queue에 추가하고 queue에서 빼내는 작업이 같다는 것을 알 수 있음.
        new Thread(producer).start();
        //starting consumer to consume messages from queue
        new Thread(consumer).start();
        System.out.println("Producer and Consumer has been started");

    }      
}