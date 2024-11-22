export interface Product {
    name: string
    target_price: number;
    image: string;
    prices: Price[];
}

export interface Price {
    price: number;
    logo: string;
}