import { useEffect } from "react";


export function useClickedOutside(ref: React.MutableRefObject<HTMLElement | null>, callback : React.Dispatch<React.SetStateAction<string>>) {
    useEffect(() => {
      
        function handleClickOutside(event: MouseEvent) {
            if (ref.current && !ref.current.contains(event.target as Node)) {
                callback("")
            }            
          }
  
      function handleKeyDown(event: KeyboardEvent) {
        if (event.key === "Escape") {
            if (ref) {
              callback("")
            }
        }
      }
  
      document.addEventListener("mousedown", handleClickOutside);
      document.addEventListener("keydown", handleKeyDown);
  
      return () => {
        document.removeEventListener("mousedown", handleClickOutside);
        document.removeEventListener("keydown", handleKeyDown);
      };
    }, [ref]);
  }
  