"use client"

import { Price } from "@/types/Product"
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowDown, faArrowUp } from '@fortawesome/free-solid-svg-icons';
import { useState } from "react";

interface Props {
    prices: Price[];
}

export default function Prices({prices}: Props) {

    const [ show, setShow ] = useState(false);

    return (
        <>
            <div>
                <ul>
                    {prices.map((price, index) =>
                        <li key={index}>{price.price}</li>
                    )}
                </ul>
            </div>
            <div className="bg-blue-500 text-2xl text-white rounded-b-lg flex justify-center items-center p-2">
                <FontAwesomeIcon icon={faArrowDown}/>
            </div>
        </>
    )
}