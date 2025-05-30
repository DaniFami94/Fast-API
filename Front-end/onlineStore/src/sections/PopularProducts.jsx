import { useRef } from "react";
import { products } from "../constants";
import PopularProductCard from "../Components/PopularProductCard";
import { useIsVisible } from "../hooks/useIsVisible";

const PopularProducts = () => {
  const ref = useRef();
  const isVisible = useIsVisible(ref);

  return (
    <section
      id="products"
      ref={ref}
      className={`max-container max-sm:mt-12 ${
        isVisible ? "animate-fade opacity-100" : "opacity-0"
      }`}
    >
      <div className="flex flex-col justify-start gap-5">
        <h2 className="text-4xl font-palanquin font-bold">
          Our <span className="text-coral-red">Popular</span> Products
        </h2>
        <p className="lg:max-w-lg mt-2 font-montserrat text-slate-gray">
          Experience top-notch quality and style with our sought-after
          selections. Discover a world of comfort, design, and value.
        </p>
        <div className="mt-16 grid lg:grid-cols-4 md:grid-cols-3 sm:grid-cols-2 grid-cols-1 sm:gap-4 gap-14">
          {products.map((product) => (
            <PopularProductCard key={product.name} {...product} />
          ))}
        </div>
      </div>
    </section>
  );
};

export default PopularProducts;
