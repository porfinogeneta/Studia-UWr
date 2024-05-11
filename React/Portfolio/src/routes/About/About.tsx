import HoverCard from "../../components/HoverCard"

export default function About() {
    const schools = [
        {
            name: "Akademickie Liceum Ogólnokształcące Politechniki Wrocławskiej",
            period: "September 2019 i May 2022",
            description: "High School, which cooperated with Politechnika Wrocławska. One of the best in the city" + 
            "in the STEM rangings"
        },
        {
            name: "University of Wrocław",
            period: "October 2022 - now",
            description: "Computer Science faculty, bechelor studies. One of the best faculties that focuses on Informatics in Poland."
        }
    ]

    const jobs = [
        {
            name: "GovTech Polska",
            period: "September 2022 - November 2022",
            description: "Internship at GovTech Poland in Technology Department." +
             "I coordinated there mutiple state-owned projects and Coorginised Hackathond for the youngsters",
            url: "src/assets/govtech.png"
        }, 
        {
            name: "Visa Technological Center",
            period: "July 2024 - September 2024",
            description: "Software Engeneer Intern at Visa's office in Warsaw.",
            url: "src/assets/visa.png"
        }
    ]

    const tech = [
        {
            photo: "src/assets/tech/react.png",
            alt: "React",
            link: "link do projektu w React"
        },
        {
            photo: "src/assets/tech/cpp.png",
            alt: "cpp",
            link: "link do projektu w C#"
        },
        {
            photo: "src/assets/tech/js.png",
            alt: "js",
            link: "link do projektu w C#"
        },
        {
            photo: "src/assets/tech/python.png",
            alt: "C#",
            link: "link do projektu w C#"
        },
        {
            photo: "src/assets/tech/scala.png",
            alt: "C#",
            link: "link do projektu w C#"
        },
        {
            photo: "src/assets/tech/sql.png",
            alt: "C#",
            link: "link do projektu w C#"
        },
        {
            photo: "src/assets/tech/vue.png",
            alt: "C#",
            link: "link do projektu w C#"
        },
        
    ]

    return (
        <div className="flex flex-col gap-16">
            <div className="mt-10">
                <img className="mt-10 w-72 mx-auto my-10" src="src/assets/circle-galata.png" alt="me"/>
                <p className="w-1/3 text-center mx-auto">
                    I'm Student of Informatics faculty on a second year of bachelor studies. My main fields of
                    interest are Web Development and Data Science.
                </p>
            </div>
            <div className="mx-auto w-full md:w-1/2 mb-20">
                <h1 className="text-7xl font-bold mb-4 w-full">Education</h1>
                <ul>
                    {schools.map((school, idx) => (
                        <li key={idx} className="mb-5">
                            <p className="italic text-slate-400 text-right mb-5">{school.period}</p>
                            <h5 className="text-xl">{school.name}</h5>
                            <p className="my-4 w-2/3 text-sm">{school.description}</p>
                        </li>
                    ))}
                </ul>
            </div>
            <div className="mx-auto w-full md:w-1/2 mb-20">
                <h1 className="text-7xl font-bold mb-10 text-left">Experience</h1>
                <div className=" grid md:grid-cols-2 grid-cols-1 justify-items-center">
                    {jobs.map((job, idx) => (
                        <HoverCard url={job.url} key={idx}>
                            <h1 className="text-left text-2xl font-bold">{job.name}</h1>
                            <p className="italic text-sm text-slate-400">{job.period}</p>
                            <p className="text-sm">{job.description}</p>
                        </HoverCard>
                    ))}
                </div>
            </div>
            <div className="mx-auto w-full md:w-1/2 mb-20">
                <h1 className="text-7xl font-bold mb-10 text-left">Tech Stack</h1>
                <div className="grid grid-cols-3 gap-4 justify-items-center">
                    {tech.map((t, idx) => (
                        <div className="w-1/2 h-1/2 transition ease-in-out  hover:-translate-y-6 hover:scale-110 duration-150" key={idx}>
                            <img src={t.photo}/>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}