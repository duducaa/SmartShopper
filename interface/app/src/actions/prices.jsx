"use server"

import axios from "axios";

export async function PricesAction(products) {

    try {
        const response = await axios.post(
            "http://smartshopper-gateway:5000/prices", 
            [{
                products: products,
                stores: ["kabum", "terabyte", "mercado-livre"]
            }],
            {
                headers: {
                    "Content-Type": "application/json",
                }
            }
        );

        const data = response.data["prices"];

        return data;
    } catch (error) {
        console.error(error);
        return {success: false}
    }
}