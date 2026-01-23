import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TaskAPITest {

    @Test
    void testAddTask() {
        TaskAPI api = new TaskAPI();
        api.addTask("New Task");
        assertTrue(api.getTasks().contains("New Task"));
    }

    @Test
    void testRemoveTask() {
        TaskAPI api = new TaskAPI();
        api.addTask("Remove Me");
        api.removeTask("Remove Me");
        assertFalse(api.getTasks().contains("Remove Me"));
    }

    @Test
    void testGetTasks() {
        TaskAPI api = new TaskAPI();
        assertEquals(3, api.getTasks().size());
    }
}
