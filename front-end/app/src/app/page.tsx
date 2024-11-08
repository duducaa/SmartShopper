"use client"

import { LoginAction } from "@/actions/login";
import Spinner from "@/components/Spinner";
import { redirect } from "next/navigation";
import { useEffect, useState, useTransition } from "react";

export default function Home() {

  const [ pwdView, setPwdView ] = useState(false);
  const [ isPending, startTransition ] = useTransition();
  const [ email, setEmail ] = useState("");
  const [ password, setPassword ] = useState("");
  const [ response, setResponse ] = useState("");
  const [ error, setError ] = useState(false);

  const changePwdView = () => setPwdView(!pwdView);

  const login = async (e: { preventDefault: () => void; }) => {
    e.preventDefault();
    const result = await LoginAction(email, password);
    if (result.key) setResponse(result.key);
    else {
      setResponse(result.key);
      setError(true);
      setTimeout(() => {
        setError(false);
      }, 1500);
    }
  }

  useEffect(() => {
    if (response == "key") {
      redirect("/home");
    }
  }, [ response ]);

  return (
    <div className="bg-gradient-to-br from-blue-500 to-blue-900 h-screen grid items-center justify-center grid-rows-6">
      <p className="text-5xl font-bold row-span-2 text-white">Smartshopper</p>
      <form action="#" className="text-gray-400 bg-white row-span-4 flex flex-col items-center rounded-md pt-10 pb-2 text-lg">
        <label htmlFor="email">Email:</label>
        <input onChange={(e) => setEmail(e.target.value)} type="text" className="border-b border-gray-500 mb-10" name="email" id="email" />
        <label htmlFor="password">Password:</label>
        <div className="relative border-b border-gray-500 mb-14">
          <input onChange={(e) => setPassword(e.target.value)} type={pwdView ? "password" : "text"} name="password" id="password" />
          <i onClick={changePwdView} className={"absolute right-0 top-1/2 -translate-y-1/2 text-gray-500 fas fa-eye" + (pwdView ? "-slash" : "")}></i>
        </div>
        <button disabled={isPending} className="bg-blue-500 rounded-md text-white px-4 py-2 mb-8" onClick={login}>{isPending ? <Spinner /> : "LOGIN"}</button>
        {error && <p className="text-red-600 font-bold mb-6">ERROR</p>}
      </form>
    </div>
  )
}
