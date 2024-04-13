import styled from "@emotion/styled"
import { BlogPostType } from "../../types/CompanyData";



const BlogcardStyle = styled.div`
    border-radius: 10px;
    padding: 20px;
    text-align: left;

    h3 {
        margin-bottom: 10px;
    }

    p {
        margin-bottom: 10px;
    }

    background-color: ${props => props.theme.blogPostBg};
    color: ${props => props.theme.text};
`

const BlogButtonStyle = styled.button`
    border: none;
    border-radius: 5px;
    cursor: pointer;
    padding: 5px 10px;
    transition: background-color 0.3s ease;
    background-color: ${props => props.theme.blogBtnBg};
    color: ${props => props.theme.btnColoredTxt};

    :hover {
        background-color: ${props => props.theme.blogBtnBgHover};
    }
`

export default function Blogcard({post}: {post: BlogPostType}) {
    return (
        <BlogcardStyle>
            <h3>{post.title}</h3>
            <p>{post.date}</p>
            <p>{post.content}</p>
            <BlogButtonStyle>Read More</BlogButtonStyle>
        </BlogcardStyle>
        
    )
}