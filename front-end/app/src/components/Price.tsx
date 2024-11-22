"use client"

import { Price } from "@/types/Product"
import { useEffect, useState } from "react";

interface Props {
    prices: Price[];
    target_price: number;
}

export default function Prices({prices, target_price}: Props) {

    const [ show, setShow ] = useState(false);
    const [ targets, setTargets ] = useState(0);

    const handleClick = () => setShow(!show);
    
    useEffect(() => {
        let count = 0;
        prices.forEach(price => {
            if (price.price <= target_price) setTargets(++count);
        });
    }, []);

    return (
        <>
            {<div className="bg-red-500 rounded-full h-10 w-10 absolute top-2 right-2 grid place-items-center text-white text-2xl">
                {targets}
            </div>}
            <div>
                {show && <ul>
                    {prices.map((price, index) =>
                        <li key={index}>{price.price}</li>
                    )}
                </ul>}
            </div>
            <div onClick={handleClick} className="bg-blue-500 text-2xl text-white rounded-b-lg flex justify-center items-center p-2">
                    <i className={"fas fa-arrow-" + (show ? "up" : "down")}></i>
            </div>
        </>
    )
}