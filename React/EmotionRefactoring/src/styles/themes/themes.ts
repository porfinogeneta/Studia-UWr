import '@emotion/react'


declare module '@emotion/react' {
  export interface Theme {
    teamMemberBg: string,
    text: string,
    buttonBg: string,
    link: string,
    navbarBg: string,
    buttonHover: string,
    toggleText: string,
    blogPostBg: string,
    blogBtnBg: string,
    contactInputBg: string,
    contactInputBorder: string,
    contactBg: string,
    contactBorder: string,
    contactBtnBg: string,
    contactBtnBgHover: string,
    btnColoredTxt: string,
    blogBtnBgHover: string,
    cardBg: string,
    background: string,
    sectionEvenBg: string
  }
}
export const theme = {
  lightTheme: {
    background: '#fff',
    themeColor: '#fff',
    text: '#333',
    toggleText: '#fff',
    link: '#333',
    buttonBg: '#333',
    buttonHover: '#555',
    cardBg: '#eee',
    teamMemberBg: '#f5f5f5',
    blogPostBg: '#f0f0f0',
    blogBtnBg: '#4caf50',
    blogBtnBgHover: '#45a049',
    sectionEvenBg: '#f5f5f5',
    navbarBg: '#f0f0f0',
    contactBg: '#f9f9f9',
    contactBorder: '#ddd',
    contactInputBg: '#fff',
    contactInputBorder: '#ccc',
    contactBtnBg: '#4caf50',
    contactBtnBgHover: '#45a049',
    btnColoredTxt: '#fff'
  },
  
  darkTheme: {
    background: '#111',
    toggleColor: '#333',
    toggleText: '#111',
    text: '#fff',
    link: '#fff',
    buttonBg: '#ddd',
    buttonHover: '#ccc',
    cardBg: '#333',
    teamMemberBg: '#444',
    blogPostBg: '#222',
    blogBtnBg: '#4caf50',
    blogBtnBgHover: '#45a049',
    sectionEvenBg: '#444',
    navbarBg: '#222',
    contactBg: '#333',
    contactBorder: '#555',
    contactInputBg: '#444',
    contactInputBorder: '#666',
    contactBtnBg: '#4caf50',
    contactBtnBgHover: '#45a049',
    btnColoredTxt: '#fff'
  }
}