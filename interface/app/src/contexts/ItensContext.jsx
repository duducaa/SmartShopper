"use client";

import { createContext, useState } from "react";


// Cria o contexto com um tipo inicial que pode ser null
export const ItensContext = createContext(null);

// Define o componente Provider com tipagem correta
export function ItensProvider({ children }) {
  const [selected, setSelected] = useState(0);

  return (
    <ItensContext.Provider value={{ selected, setSelected }}>
      {children}
    </ItensContext.Provider>
  );
}