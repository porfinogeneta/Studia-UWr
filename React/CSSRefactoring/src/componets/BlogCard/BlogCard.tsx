import { BlogPostType } from "../../types/CompanyData";

import classes from "./styles.module.scss"

export default function Blogcard({post}: {post: BlogPostType}) {
    return (
        <div key={post.id} className={classes.blog_post}>
            <h3>{post.title}</h3>
            <p>{post.date}</p>
            <p>{post.content}</p>
            <button>Read More</button>
        </div>
        
    )
}