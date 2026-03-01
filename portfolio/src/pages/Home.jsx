import { ThemeToggle } from "../components/ThemeToggle";
import { StarBackground } from "@/components/StarBackground";
import { Navbar } from "../components/Navbar"

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

  {/* Footer */}

  </div>
  );
};
