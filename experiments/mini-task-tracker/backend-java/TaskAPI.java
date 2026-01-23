import java.util.ArrayList;
import java.util.List;

public class TaskAPI {

    private List<String> tasks;

    public TaskAPI() {
        tasks = new ArrayList<>();
        tasks.add("Learn Java");
        tasks.add("Build frontend");
        tasks.add("Test Python client");
    }

    public List<String> getTasks() {
        return tasks;
    }

    public void addTask(String task) {
        tasks.add(task);
    }

    public void removeTask(String task) {
        tasks.remove(task);
    }

    // Main for quick testing
    public static void main(String[] args) {
        TaskAPI api = new TaskAPI();
        System.out.println("Tasks: " + api.getTasks());
    }
}
