"use server"

import axios from "axios";

export async function HistoryAction(userId) {

    try {
        const response = await axios.post(
            "http://smartshopper-gateway:5000/history", 
            [{user_id: userId}],
            {
                headers: {
                    "Content-Type": "application/json",
                }
            }
        );

        const data = response.data["history"];

        return data;
    } catch (error) {
        console.error(error);
        return {success: false}
    }
}