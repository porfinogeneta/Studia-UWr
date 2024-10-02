import { expect, describe, it, vi } from "vitest";
import { fireEvent, render, screen } from '@testing-library/react';
import { TodosContext } from "../../providers/TodosProvider/TodosProvider";
import { ITodo } from "../../types/ITodo.type";
import TodoGrid from "./TodoGrid";

describe("TodoGrid Component", () => {
    const addTodo = vi.fn()
    const editTodo = vi.fn()
    const removeTodo = vi.fn()
  
  
    interface IProps {
      children: React.ReactNode;
    }
  
    const TestProvider = ({children}: IProps) => {
  
  
      const initialTodos: ITodo[] = [{
        id: "1",
        name: "Test Name 1",
        priority: "medium",
        createdAt: new Date(),
        updatedAt: new Date(),
        status: "done",
        tags: ["personal", "work"],
      },
      {
        id: "2",
        name: "Test Name 2",
        priority: "high",
        createdAt: new Date(),
        updatedAt: new Date(),
        status: "in-progress",
        tags: ["education", "travel"]
      },
      {
        id: "3",
        name: "Test Name 3",
        priority: "low",
        createdAt: new Date(),
        updatedAt: new Date(),
        status: "to-do",
        tags: ["university", "travel"]
      }
    ]
  
      
  
      return (
        <TodosContext.Provider value={{todos: initialTodos, addTodo, removeTodo, editTodo}}>
          {children}
        </TodosContext.Provider>
      )
    }
  
    it("checks if component was properly rendered", () => {
      render(
        <TestProvider>
          <TodoGrid/>
        </TestProvider>
      )
      
      expect(screen.getAllByRole("row")).toHaveLength(4) // 1 todo with status 'done' + header row
    })
  
    it("checks if delete function works properly", () => {
      render(
        <TestProvider>
          <TodoGrid/>
        </TestProvider>
      )
  
  
      fireEvent.click(screen.getAllByLabelText("Delete")[0])
      expect(removeTodo).toHaveBeenCalledWith("1")
    })
  
    it("checks if edit function works properly", () => {
      render(
        <TestProvider>
          <TodoGrid/>
        </TestProvider>
      )
  
      fireEvent.click(screen.getAllByLabelText("Edit")[0])
      // change status
      const statusSelect = screen.getByText("Done")
      fireEvent.mouseDown(statusSelect)
      fireEvent.click(screen.getAllByText("In Progress")[0])
      // change priotity
      const prioritySelect = screen.getByText("Medium")
      fireEvent.mouseDown(prioritySelect)
      fireEvent.click(screen.getAllByText("High")[0])
      // save changes
      const saveButton = screen.getByLabelText("Save");
      fireEvent.click(saveButton);
  
  
      expect(editTodo).toHaveBeenCalledWith("1", {
             "priority": "medium",
             "status": "done",
          })
  
    })
  
    it("checks that no edit is done when cancelled", () => {
      render(
        <TestProvider>
          <TodoGrid/>
        </TestProvider>
      )
  
      fireEvent.click(screen.getAllByLabelText("Edit")[0])
      // change status
      const statusSelect = screen.getByText("Done")
      fireEvent.mouseDown(statusSelect)
      fireEvent.click(screen.getAllByText("In Progress")[0])
      // change priotity
      const prioritySelect = screen.getByText("Medium")
      fireEvent.mouseDown(prioritySelect)
      fireEvent.click(screen.getAllByText("High")[0])
      // save changes
      const saveButton = screen.getByLabelText("Cancel");
      fireEvent.click(saveButton);
  
      expect(editTodo).toHaveBeenCalledWith("1", {"status": "done", "priority": "medium"})
      
    })
  
  })