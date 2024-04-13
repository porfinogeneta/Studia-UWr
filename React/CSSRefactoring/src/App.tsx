import { useState } from "react";
import "./App.scss";

// components
import Navbar from "./componets/Navbar/Navbar"
import Header from "./componets/Header/Header";
import TeamCard from "./componets/TeamCard/TeamCard";
import Section from "./Section/Section";
import Blogcard from "./componets/BlogCard/BlogCard";
import ContactForm from "./componets/ContactForm/ContactForm";
import Footer from "./componets/Footer/Footer";

const companyData = {
  name: "Acme Corporation",
  slogan: "Innovation at its best",
  about:
    "We are a leading provider of innovative solutions in various industries. Our team is dedicated to delivering high-quality products and services to our clients worldwide.",
  services: [
    {
      id: 1,
      name: "Web Development",
      description: "Creating modern and responsive websites.",
    },
    {
      id: 2,
      name: "Mobile App Development",
      description: "Building mobile applications for iOS and Android.",
    },
    {
      id: 3,
      name: "UI/UX Design",
      description:
        "Designing intuitive user interfaces for optimal user experience.",
    },
    {
      id: 4,
      name: "Digital Marketing",
      description:
        "Promoting products and services through various online channels.",
    },
  ],
  teamMembers: [
    {
      id: 1,
      name: "Alice Young",
      position: "CEO",
      bio: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis libero et nisi cursus, sit amet laoreet odio rutrum.",
      image: "https://via.placeholder.com/150",
    },
    {
      id: 2,
      name: "Jane Smith",
      position: "CTO",
      bio: "Duis aliquam purus ac ante volutpat, nec lobortis tortor sagittis. Sed finibus eleifend efficitur.",
      image: "https://via.placeholder.com/150",
    },
    {
      id: 3,
      name: "Alice Johnson",
      position: "Lead Designer",
      bio: "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris consectetur, velit et efficitur fringilla, ligula felis dignissim.",
      image: "https://via.placeholder.com/150",
    },
  ],
  blogPosts: [
    {
      id: 1,
      title: "The Future of Technology",
      date: "March 10, 2024",
      content:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis libero et nisi cursus, sit amet laoreet odio rutrum.",
    },
    {
      id: 2,
      title: "Design Trends for 2024",
      date: "February 28, 2024",
      content:
        "Duis aliquam purus ac ante volutpat, nec lobortis tortor sagittis. Sed finibus eleifend efficitur.",
    },
    {
      id: 3,
      title: "The Power of Social Media",
      date: "February 15, 2024",
      content:
        "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris consectetur, velit et efficitur fringilla, ligula felis dignissim.",
    },
    {
      id: 4,
      title: "Artificial Intelligence in Business",
      date: "January 30, 2024",
      content:
        "Suspendisse eget sapien vitae eros tincidunt ultrices. Morbi nec sem nisi. Nulla ultrices odio et eros varius, a eleifend velit tristique.",
    },
    {
      id: 5,
      title: "The Impact of Virtual Reality",
      date: "January 15, 2024",
      content:
        "Integer auctor neque mauris, eget sagittis justo tristique sit amet. Nam at nibh et nulla suscipit blandit eu nec mi.",
    },
  ],
};

const App = () => {
  
  const [darkMode, setDarkMode] = useState(false);

  const toggleTheme = (mode: boolean) => {
    setDarkMode(!mode);
  };

  return (
    <div className={`portfolio ${darkMode ? "dark-theme" : "light-theme"}`}>
      <Navbar toggleTheme={toggleTheme}/>
      <Header darkMode={darkMode} children={{name: companyData.name, slogan: companyData.slogan}}/>
      <div className="content-card">
        <Section id="about" title={"About Us"}>
          <p>{companyData.about}</p>
        </Section>
        <Section id="services" title={"Our Services"}>
          <div className="services">
            <ul>
                {companyData.services.map((service) => (
                  <li key={service.id}>
                    <h3>{service.name}</h3>
                    <p>{service.description}</p>
                  </li>
                ))}
              </ul>
          </div>
        </Section>
        <Section id="team" title={"Meet Out Team"}>
            <div className="team-members">
              {companyData.teamMembers.map((member) => (
                <TeamCard darkMode={darkMode} key={member.id} member={member}/>
              ))}
            </div>
        </Section>
        <Section id="blog" title="Latest Blog Posts">
          <div className="blog-posts">
              {companyData.blogPosts.map((post) => (
                  <Blogcard post={post}/>
                ))}
          </div>
        </Section>
        <Section id="contact" title="Contact Us">
            <ContactForm/>
        </Section>
      </div>
      <Footer name={companyData.name}/>
    </div>
  );
};

export default App;
