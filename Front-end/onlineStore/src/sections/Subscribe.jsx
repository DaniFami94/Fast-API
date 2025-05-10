import { arrowRight } from "../assets/icons";
import Button from "../Components/Button";
import { useRef } from "react";
import { useIsVisible } from "../hooks/useIsVisible";

const Subscribe = () => {
  const ref = useRef();
  const isVisible = useIsVisible(ref);
  return (
    <section
      id="contact-us"
      ref={ref}
      className={`max-container flex flex-col justify-between items-center gap-10 ${
        isVisible ? "animate-fade opacity-100" : "opacity-0"
      }`}
    >
      <h3 className="text-4xl leading-[68px] lg:max-w-md font-palanquin font-bold">
        Sign Up for <span className="text-coral-red"> Updates </span>&
        Newsletter
      </h3>

      <div className="lg:max-w-[40%] w-full flex items-center max-sm:flex-col gap-5 p-2.5 sm:border sm:border-slate-gray rounded-full">
        <input type="text" placeholder="subscribe@nike.com" className="input" />
        <div className="flex max-sm:justify-end items-center max-sm:w-full">
          <Button label="Sign Up" fullWidth iconURL={arrowRight} />
        </div>
      </div>
    </section>
  );
};

export default Subscribe;
