"use client"

import { PricesAction } from "../../actions/prices";
import { ProductsAction } from "../../actions/products";
import LineChart from "../../components/Chart";
import Price from "../../components/Price";
import { UserContext } from "../../contexts/UserContext";
import Image from "next/image";
import { useContext, useEffect, useState } from "react";
import { ItensProvider } from "../../contexts/ItensContext";

export default function Home() {

    const userContext = useContext(UserContext);
    if (!userContext) return <p></p>
    const { userId } = userContext;
    const [ products, setProducts ] = useState([]);
    const [ prices, setPrices ] = useState([]);
    const [ priceHistory, setPriceHistory ] = useState([]);

    const getProducts = async () => {
        const result = await ProductsAction(userId);
        setProducts(result);
    }

    const getPrices = async () => {
        const result = await PricesAction(products);
        Object.entries(result).forEach(([product, _prices]) => {
            result[product]["mercado_livre"] = result[product]["mercado-livre"];
            delete result[product]["mercado-livre"];
        });
        setPrices(result);
    }

    const getPriceHistory = async () => {
        const result = await HistoryAction(userId);
        setPriceHistory(result);
    }

    useEffect(() => {
        getProducts();
    }, []);

    useEffect(() => {
        getPrices();
        getPriceHistory();
    }, [ products ]);

    return (
        <>
            <header className="bg-blue-500 text-white font-bold text-3xl p-3">
                <p>Smartshopper</p>
            </header>
            <main className="pt-5 px-5 text-black">
                <ItensProvider>
                    <List products={products}  />
                    <LineChart priceHistory={priceHistory} />
                </ItensProvider>
            </main>
            <footer className="bg-blue-500 text-white">

            </footer>
        </>
    );
}

function List({ products }) {

    return (
        <ul className="grid grid-flow-col cols overflow-x-scroll scrollbar-hide gap-4">{products.map((product, index) => 
            <li className="relative" key={index}>
                <div className="bg-blue-500 p-5 w-60 rounded-t-lg">
                    {/* <Image src={product.image}
                    alt=""
                    height={200}
                    width={200}
                    className="rounded-lg"/> */}
                    <p className="text-white font-bold text-2xl text-center mt-6">{product.name}</p>
                    <p className="text-white font-bold text-2xl text-center mt-6">R$ {product.target_price},00</p>
                </div>
                <Price prices={prices[product.name]} target_price={product.target_price} />
            </li>
        )}</ul>
    )
}