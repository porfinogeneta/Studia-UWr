import {expect, test} from "vitest"
import { todosReducer } from "./todosReducer"
import { IBaseTodoFields, ITodo } from "../../types/ITodo.type"
import { ITodoAction } from "./todosReducer"


test("Add Action", () => {

    const initialState: ITodo[] = []

    const newTodo: Omit<IBaseTodoFields, "status"> = {
        name: "Dummy",
        priority: "medium",
        tags: ["health"]
    }
    const action: ITodoAction = {
        type: "ADD_TODO",
        payload: newTodo
    }

    const result = todosReducer(initialState, action)
    expect(result.length).toBe(1)
    expect(result[0]).toEqual({
        id: expect.any(String),
        name: "Dummy",
        status: "to-do",
        priority: "medium",
        createdAt: expect.any(Date),//mock date
        updatedAt: expect.any(Date),
        tags: ["health"],
      });
})

test("Remove Action", () => {
    const initialState: ITodo[] = [    { id: "1", name: "Dummy", status: "to-do", priority: "medium", createdAt: new Date(), updatedAt: new Date(), tags: ["health"] }]
    const action: ITodoAction = {
        type: "REMOVE_TODO",
        payload: "1"
    }

    const result = todosReducer(initialState, action)
    expect(result.length).toBe(0)
})

test("Set Name", () => {
    const initialState: ITodo[] = [{ id: "1", name: "Dummy", status: "to-do", priority: "medium", createdAt: new Date(), updatedAt: new Date(), tags: ["health"] }]
    const action: ITodoAction = {
        type: "SET_NAME",
        payload: {
            id: "1",
            name: "New Name"
        }
    }

    const result = todosReducer(initialState, action)
    expect(result[0].name).toBe("New Name")
    expect(result[0].updatedAt).toBeInstanceOf(Date)

})


test("Set Status", () => {
    const initialState: ITodo[] = [{ id: "1", name: "Dummy", status: "to-do", priority: "medium", createdAt: new Date(), updatedAt: new Date(), tags: ["health"] }]
    const action: ITodoAction = {
        type: "SET_STATUS",
        payload: {
            id: "1",
            status: "in-progress"
        }
    }

    const result = todosReducer(initialState, action)
    expect(result[0].status).toBe("in-progress")
    expect(result[0].updatedAt).toBeInstanceOf(Date)
})

test("Set Priority", () => {
    const initialState: ITodo[] = [{ id: "1", name: "Dummy", status: "to-do", priority: "medium", createdAt: new Date(), updatedAt: new Date(), tags: ["health"] }]
    const action: ITodoAction = {
        type: "SET_PRIORITY",
        payload: {
            id: "1",
            priority: "low"
        }
    }

    const result = todosReducer(initialState, action)
    expect(result[0].priority).toBe("low")
    expect(result[0].updatedAt).toBeInstanceOf(Date)
})

test("Set Tags", () => {
    const initialState: ITodo[] = [{ id: "1", name: "Dummy", status: "to-do", priority: "medium", createdAt: new Date(), updatedAt: new Date(), tags: ["health"] }]
    const action: ITodoAction = {
        type: "SET_TAGS",
        payload: {
            id: "1",
            tags: ["writing", "meditation"]
        }
    }

    const result = todosReducer(initialState, action)
    expect(result[0].tags).toEqual(["writing", "meditation"])
    expect(result[0].updatedAt).toBeInstanceOf(Date)
})

// Add, Set Priority, and Set Tags
test("Combined Actions: Add, Set Priority, and Set Tags", () => {
    const initialState: ITodo[] = [];
  
    const newTodo: Omit<IBaseTodoFields, "status"> = {
      name: "Dummy",
      priority: "medium",
      tags: ["health"]
    };
    const addAction: ITodoAction = {
      type: "ADD_TODO",
      payload: newTodo
    };
  
    let result = todosReducer(initialState, addAction);
    const addedTodoId = result[0].id;
  
    const setPriorityAction: ITodoAction = {
      type: "SET_PRIORITY",
      payload: {
        id: addedTodoId,
        priority: "low"
      }
    };
  
    result = todosReducer(result, setPriorityAction);
  
    const setTagsAction: ITodoAction = {
      type: "SET_TAGS",
      payload: {
        id: addedTodoId,
        tags: ["writing", "meditation"]
      }
    };
  
    result = todosReducer(result, setTagsAction);
  
    expect(result.length).toBe(1);
    expect(result[0].priority).toBe("low");
    expect(result[0].tags).toEqual(["writing", "meditation"]);
  });
  