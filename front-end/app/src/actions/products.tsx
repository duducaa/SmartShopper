"use server"

import axios from "axios";
import { cookies } from "next/headers";

export async function ProductsAction() {
    
    const cookieStore = cookies();
    const user = cookieStore.get("user");
    
    console.log(user)
    if (user) {
        try {
            const response = await axios.post(
                "http://smartshopper-gateway:5000/products", 
                [{user_id: user.value}]);
            const data = response.data;
            return data["products"];
        } catch (error) {
            console.error(error);
            return {success: false}
        }
    }
}