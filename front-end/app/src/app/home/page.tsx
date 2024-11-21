import Price from "@/components/Price";
import { Product } from "@/types/Product";
import axios from "axios";
import Image from "next/image";

export default async function Home() {

    const BASE_URL = "http://smartshopper-scraping-gateway:5000";
    const response = await axios.get(BASE_URL + "/");
    const products: Product[] = response.data["products"];

    return (
        <>
            <header className="bg-blue-500 text-white font-bold text-3xl p-3">
                <p>Smartshopper</p>
            </header>
            <main className="pt-5 ps-5 text-black">
                <ul className="grid grid-flow-col cols overflow-x-auto gap-4">{products.map((product, index: number) => 
                    <li className="relative" key={index}>
                        <div className="bg-blue-500 p-5 w-60 rounded-t-lg">
                            <Image src={product.image}
                            alt=""
                            height={200}
                            width={200}
                            className="rounded-lg"/>
                            <p className="text-white font-bold text-2xl text-center mt-6">{product.name}</p>
                            <p className="text-white font-bold text-2xl text-center mt-6">R$ {product.target_price},00</p>
                        </div>
                        <Price prices={product.prices} target_price={product.target_price} />
                    </li>
                )}</ul>
            </main>
            <footer className="bg-blue-500 text-white">

            </footer>
        </>
    );
}