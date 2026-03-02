import { ThemeToggle } from "../components/ThemeToggle";
import { StarBackground } from "@/components/StarBackground";
import { Navbar } from "../components/Navbar";
import { HeroSection } from "../components/HeroSection.jsx";
import { AboutSection } from "../components/AboutSection.jsx";

export const Home = () => {
  return  ( 
    <div className="min-h-screen bg-background text-foreground  overflow-x-hidden">

  {/* Theme toggle dark light mode */}
  <ThemeToggle />

  {/* Background Effects */}
  <StarBackground />

  {/* Navbar navigation */}
  <Navbar />

  {/* Main Content */}
  <main>
    <HeroSection />
    <AboutSection />
  </main>

  {/* Footer */}

  </div>
  );
};
