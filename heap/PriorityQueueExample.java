import java.util.PriorityQueue;
import java.util.Comparator;

public class PriorityQueueExample {
    public static void main(String[] args) {
        // Default PriorityQueue (Min-Heap - smallest element has highest priority)
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        minHeap.offer(5);
        minHeap.offer(1);
        minHeap.offer(3);
        minHeap.offer(2);

        System.out.println("Min-Heap:");
        while (!minHeap.isEmpty()) {
            System.out.print(minHeap.poll() + " "); // Output: 1 2 3 5
        }
        System.out.println();


        // Max-Heap (largest element has highest priority) using a custom comparator
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        maxHeap.offer(5);
        maxHeap.offer(1);
        maxHeap.offer(3);
        maxHeap.offer(2);

        System.out.println("Max-Heap:");
        while (!maxHeap.isEmpty()) {
            System.out.print(maxHeap.poll() + " "); // Output: 5 3 2 1
        }
        System.out.println();

        // PriorityQueue with custom objects and a comparator
        PriorityQueue<Task> taskQueue = new PriorityQueue<>(Comparator.comparingInt(Task::getPriority));

        taskQueue.offer(new Task("Low Priority Task", 3));
        taskQueue.offer(new Task("High Priority Task", 1));
        taskQueue.offer(new Task("Medium Priority Task", 2));

        System.out.println("Task Queue (Priority based):");
        while (!taskQueue.isEmpty()) {
            System.out.println(taskQueue.poll().getName());
        }

    }
}

class Task {
    private String name;
    private int priority;

    public Task(String name, int priority) {
        this.name = name;
        this.priority = priority;
    }

    public String getName() {
        return name;
    }

    public int getPriority() {
        return priority;
    }
}