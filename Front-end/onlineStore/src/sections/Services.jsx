import { services } from "../constants";
import ServiceCard from "../Components/ServiceCard";
import { useRef } from "react";
import { useIsVisible } from "../hooks/useIsVisible";
const Services = () => {
  const ref = useRef();
  const isVisible = useIsVisible(ref);
  return (
    <section
      ref={ref}
      className={`max-container flex justify-center flex-wrap gap-9 ${
        isVisible ? "animate-fade opacity-100" : "opacity-0"
      }`}
    >
      {services.map((service) => (
        <ServiceCard key={service.label} {...service} />
      ))}
    </section>
  );
};

export default Services;
