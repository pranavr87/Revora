import LandingNavbar from "../components/LandingNavbar";
import Hero from "../components/Hero";
import WhyRevora from "../components/WhyRevora";
import HowItWorks from "../components/HowItWorks";

function Landing() {

    return (

        <>

            <LandingNavbar />

            <Hero />

            <section id="why">

                <WhyRevora />

            </section>

            <HowItWorks />

        </>

    );

}

export default Landing;