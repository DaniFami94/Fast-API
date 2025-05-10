import Button from "../Components/Button";
import { arrowRight } from "../assets/icons";
import { shoe8 } from "../assets/images";
import { useRef } from "react";
import { useIsVisible } from "../hooks/useIsVisible";

const SuperQuality = () => {
  const ref = useRef();
  const isVisible = useIsVisible(ref);
  return (
    <section
      id="about-us"
      ref={ref}
      className={`flex justify-between items-center max-lg:flex-col gap-10 w-full max-container ${
        isVisible ? "animate-fade opacity-100" : "opacity-0"
      }`}
    >
      <div className="flex flex-1 flex-col">
        <h2 className="font-palanquin text-4xl capitalize font-bold lg:max-w-lg">
          We Provide You
          <span className="text-coral-red"> Super </span>
          <span className="text-coral-red"> Quality </span>Shoes
        </h2>
        <p className="mt-4 lg:max-w-lg info-text">
          Ensuring premium comfort and style, our meticulously crafted footwear
          is designed to elevate your experience, providing your with unmatched
          quality, innovation, and a touch of elegance.
        </p>
        <p className="mt-6 lg:max-w-lg info-text">
          Our dedication to detail and excellence ensures your satisfaction
        </p>
        <div className="mt-11">
          <Button label="View details" iconURL={arrowRight} />
        </div>
      </div>

      <div className="flex-1 flex justify-center items-center">
        <img
          src={shoe8}
          alt="shoe8"
          width={570}
          height={522}
          className="object-contain"
        />
      </div>
    </section>
  );
};

export default SuperQuality;
