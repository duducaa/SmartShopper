pragma foreign_keys = on;

create table desired_products (
    product_id integer primary key autoincrement,
    product_name text,
    target_price decimal(10, 2),
    image_path text
);

create table stores (
    store_id integer primary key autoincrement,
    store_name text,
    logo_path text
);

create table prices (
    price_id integer primary key autoincrement,
    store_id integer,
    product_id integer,
    price decimal(10, 2),
    foreign key (store_id) references stores(store_id) on delete cascade on update cascade,
    foreign key (product_id) references desired_products(product_id) on delete cascade on update cascade
);

insert into desired_products
values
(1, "GTX 1650", 3700.00, "https://m.media-amazon.com/images/I/71qK2pMmqnL.jpg"),
(2, "i7-12700", 2500.00, "https://cdn.shoppub.io/cdn-cgi/image/w=1000,h=1000,q=80,f=auto/oficinadosbits/media/uploads/produtos/foto/ctawpcbc/file.png"),
(3, "Monitor FUll HD", 890.00, "https://images.tcdn.com.br/img/img_prod/740836/monitor_gamer_pcfort_t2701_165_27_led_full_hd_165hz_display_port_hdmi_dvi_vesa_13891_4_1f6b1005568d2b5888a9ba6e8920b578.jpg"),
(4, "RAM 3200 MHz", 300.00, "https://cdn.awsli.com.br/2500x2500/2557/2557636/produto/260980923/memoria-kingston-fury-impact-8gb-3200mhz-ddr4-cl20-para-notebook-kf432s20ib-8_16-tyloibza7x.jpg"),
(5, "SSD KC3000", 700.00, "https://www.kingstonstore.com.br/cdn/shop/products/KC3000500G4_1200x.jpg?v=1635368025");

insert into stores
values
(1, "Kabum", "https://t.ctcdn.com.br/luOODOyEQXWKBMiGRDleaCrJzyE=/i490135.jpeg"),
(2, "Terabyte", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRi0XeV12_6bpTmt3x0__wr4vxB8R730xtnWQ&s"),
(3, "Mercado Livre", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8aG4jVaHz3yj8t0KbCz6qXmc5bD9hkvtr_A&s");

insert into prices
values
(1, 1, 1, 4000),
(2, 1, 2, 2600),
(3, 1, 3, 1200),
(4, 1, 4, 520),
(5, 1, 5, 1000),

(6, 2, 1, 4100),
(7, 2, 2, 2700),
(8, 2, 3, 1100),
(9, 2, 4, 500),
(10, 2, 5, 800),

(11, 3, 1, 4200),
(12, 3, 2, 2800),
(13, 3, 3, 1060),
(14, 3, 4, 480),
(15, 3, 5, 780);