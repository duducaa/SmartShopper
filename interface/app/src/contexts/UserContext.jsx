"use client";

import { createContext, useState } from "react";


// Cria o contexto com um tipo inicial que pode ser null
export const UserContext = createContext(null);

// Define o componente Provider com tipagem correta
export function UserProvider({ children }) {
  const [userId, setUserId] = useState(-1);

  return (
    <UserContext.Provider value={{ userId, setUserId }}>
      {children}
    </UserContext.Provider>
  );
}