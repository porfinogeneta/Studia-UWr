import { NavLink, Outlet, useLocation } from "react-router-dom";


export default function RootLayout() {
    const location = useLocation();
    return (
        <div className="font-mono bg-slate-900 text-slate-50">
            <nav className="bg-slate-800 py-4 ">
                <ul className="flex justify-center gap-6">
                    <li>
                        <NavLink
                        to="/"
                        className={({ isActive }) => `${isActive ? "underline" : ""}`}
                        state={{ from: location.pathname }}
                        >
                        Home
                        </NavLink>
                    </li>
                    <li>
                        <NavLink
                        to="/about"
                        className={({ isActive }) => `${isActive ? "underline" : ""}`}
                        
                    <li>
                        <NavLink
                        to="/projects"
                        className={({ isActive }) => `${isActive ? "underline" : ""}`}
                        state={{ from: location.pathname }}
                        >
                        Projects
                        </NavLink>
                    </li>
                    <li>
                        <NavLink
                        to="/side-project"
                        className={({ isActive }) => `${isActive ? "underline" : ""}`}
                        state={{ from: location.pathname }}
                        >
                        Side Project
                        </NavLink>
                    </li>
                </ul>
            </nav>
        <main>
            <Outlet />
        </main>
        <footer className="py-4 text-center bg-slate-800">
            <p>© 2024 Szymon Mazurek</p>
        </footer>
    </div>
    )
}
