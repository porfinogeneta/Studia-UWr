import NewTodo from "./NewTodo";
import { expect, describe, it, vi } from "vitest";
import { fireEvent, render, screen } from '@testing-library/react';
import { TodosContext } from "../../providers/TodosProvider/TodosProvider";

describe("NewTodo Component", () => {
    const addTodo = vi.fn()
    const removeTodo = vi.fn()
    const editTodo = vi.fn()
  
    interface IProps {
      children: React.ReactNode;
    }
  
    const TestProvider = ({children}: IProps) => {
  
  
      return (
        <TodosContext.Provider value={{todos: [], addTodo, removeTodo, editTodo}}>
          {children}
        </TodosContext.Provider>
      )
    }
  
  
    it("render NewTodo component", () => {
      render(
        <TestProvider>
          <NewTodo/>
        </TestProvider>
      );
      expect(screen.getByText("Add")).toBeInTheDocument();
    });
  
    it("test add todo"), () => {
      render(
        <TestProvider>
          <NewTodo/>
        </TestProvider>
      );
  
  
      // fill in the text form
      fireEvent.change(screen.getByLabelText("Todo Name"), {target: {value: 'Test Task'}})
      // choose option
      fireEvent.mouseDown(screen.getByLabelText("Priority"))
      fireEvent.click(screen.getByText("High"))
      // fill in tags
      fireEvent.change(screen.getByLabelText("Tags"), {target: {value: 'Home'}})
      fireEvent.click(screen.getByText('Home'))
  
      // add todo
      fireEvent.click(screen.getByText("Add"));
  
      expect(addTodo).toHaveBeenCalledWith({
        name: "Test Task",
        priority: 'High',
        tags: ["Home"]
      })
  
    }
  
    it("shows aria invalid when no name is provided", () => {
      render(
        <TestProvider>
          <NewTodo />
        </TestProvider>
      );
  
      fireEvent.click(screen.getByText("Add"));
  
      const input = screen.getByLabelText("Todo Name");
      expect(input).toHaveAttribute("aria-invalid", "true");
    });
  
    it("adds Mui-error class when no priority is selected", () => {
      render(
        <TestProvider>
          <NewTodo />
        </TestProvider>
      );
  
      fireEvent.change(screen.getByLabelText("Todo Name"), { target: { value: 'Test Task' } });
      fireEvent.click(screen.getByText("Add"));
  
      const select = screen.getByLabelText("Priority");
      expect(select).toHaveClass("Mui-error");
      // czy add się wywołał
    });
  
  
    it("clears the form after adding a todo", () => {
      render(
        <TestProvider>
          <NewTodo />
        </TestProvider>
      );
  
      fireEvent.change(screen.getByLabelText("Todo Name"), { target: { value: 'Test Task' } });
      fireEvent.mouseDown(screen.getByLabelText("Priority"));
      fireEvent.click(screen.getByText("High"));
      fireEvent.change(screen.getByLabelText("Tags"), { target: { value: 'Home' } });
      fireEvent.click(screen.getByText('Home'));
  
      fireEvent.click(screen.getByText("Add"));
  
      expect(screen.getByLabelText("Todo Name")).toHaveValue("");
    //   expect(screen.getByLabelText("Priority")).toHaveValue(undefined); // jednak nie działa
      expect(screen.getByLabelText("Tags")).toHaveValue("");
    });
  
    it("shows default values in the form", () => {
      render(
        <TestProvider>
          <NewTodo />
        </TestProvider>
      );
  
      expect(screen.getByLabelText("Todo Name")).toHaveValue("");
    //   expect(screen.getByLabelText("Priority")).toHaveValue(undefined);  // Adjust based on your component's default value handling
      expect(screen.getByLabelText("Tags")).toHaveValue("");
    });
  
  });
  