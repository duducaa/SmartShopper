"use server"

import axios from "axios";

export async function LoginAction(email, password) {

    try {
        const response = await axios.post(
            "http://smartshopper-gateway:5000/login", 
            [{ email, password }]
        );
        
        const data = response.data;

        return data;
    } catch (error) {
        console.error(error);
        return {success: false}
    }
}