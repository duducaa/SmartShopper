"use server"

import axios from "axios";
import { cookies } from "next/headers"

export async function LoginAction(email: string, password: string) {

    const cookieStore = cookies();

    try {
        const response = await axios.post(
            "http://smartshopper-gateway:5000/login", 
            [{email: email, password: password}],
            {
                headers: {
                    "Content-Type": "application/json",
                }
            })
        const data = response.data;
        
        cookieStore.set('user', JSON.stringify({"id": data.user_id}), {
            httpOnly: true,
            secure: process.env.NODE_ENV === 'production',
            maxAge: 60 * 60 * 24 * 7,
            path: '/',
          });

        return data;
    } catch (error) {
        console.error(error);
        return {success: false}
    }
}