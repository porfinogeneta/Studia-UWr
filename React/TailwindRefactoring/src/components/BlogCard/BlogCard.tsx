import { BlogPostType } from "../../types/CompanyData";



export default function Blogcard({post}: {post: BlogPostType}) {
    return (
        <div className="rounded-lg p-4 text-left bg-gray-300 dark:bg-gray-800">
            <h3 className="text-lg font-semibold mb-2">{post.title}</h3>
            <p className="text-base mb-2">{post.date}</p>
            <p className="text-base mb-4">{post.content}</p>
            <button className="text-sm border-none rounded-md cursor-pointer py-1 px-4
             transition-colors duration-300 bg-green-600 text-white hover:bg-green-700">
                Read More
            </button>
        </div>
        
    )
}