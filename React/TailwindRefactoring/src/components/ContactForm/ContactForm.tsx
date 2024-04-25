

export default function ContactForm() {

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
      };

    return (
        <form className="max-w-md mx-auto mb-10 px-4 py-6 bg-gray-100 rounded-lg flex flex-col" onSubmit={handleSubmit}>
            <div className="mb-4">
                <input type="text" placeholder="Name" className="w-full p-2 border border-gray-300 rounded" required />
            </div>
            <div className="mb-4">
                <input type="email" placeholder="Email" className="w-full p-2 border border-gray-300 rounded" required />
            </div>
            <div className="mb-4">
                <textarea rows={5} placeholder="Message" className="w-full p-2 border border-gray-300 rounded resize-y" required></textarea>
            </div>
            <button type="submit" className="py-2 px-4 
            rounded cursor-pointer transition-colors 
            duration-300  bg-green-600 text-white hover:bg-green-700">Send Message</button>
        </form>
    )
}