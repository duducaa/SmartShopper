"use server"

export async function LoginAction(email: string, password: string) {
    try {
        const response = await fetch("http://smartshopper_flask:5000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify([{email: email, password: password}])
        });
        const data = await response.json();
        return data
    } catch (error) {
        console.error(error);
        return {success: false}
    }
}