import "./globals.css";
import React from "react";
import { UserProvider } from "../contexts/UserContext";

export const metadata = {
  title: "Smartshopper",
};

export default function RootLayout({
  children,
}) {
  return (
    <html lang="en">
      <body>
        <UserProvider>
          {children}
        </UserProvider>
      </body>
    </html>
  );
}
