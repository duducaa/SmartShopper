"use server"

import axios from "axios";

export async function ProductsAction(userId) {

    try {
        const response = await axios.post(
            "http://smartshopper-gateway:5000/products", 
            [{user_id: userId}],
            {
                headers: {
                    "Content-Type": "application/json",
                }
            }
        );

        const data = response.data["products"];

        return data;
    } catch (error) {
        console.error(error);
        return {success: false}
    }
}