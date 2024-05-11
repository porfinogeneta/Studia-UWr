import { useRouteError } from "react-router-dom";


interface RouteError {
    data: string;
    error: {
      columnNumber: number;
      fileName: string;
      lineNumber: number;
      message: string;
      stack: string;
    };
    internal: boolean;
    status: number;
    statusText: string;
  }

export default function NotFound() {
    const error = useRouteError() as RouteError

    return (
        <div className="text-slate-200">
            <h1>Oops!</h1>
            <p>Sorry, an unexpected error has occurred.</p>
            <p>
                <i>{error.statusText || error.error.message}</i>
            </p>
        </div>
    );
}