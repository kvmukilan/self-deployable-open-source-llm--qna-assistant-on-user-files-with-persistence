css = '''
<style>
.chat-message {
    padding: 0.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 5%;
}
.chat-message .avatar img {
  max-width: 50px;
  max-height: 50x;
  border-radius: 25%;
  object-fit: cover;
}
.chat-message .message {
  width: 50%;
  padding: 0 0.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 50px; max-width: 50px; border-radius: 25%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIYAAACGCAMAAAAvpwKjAAAAY1BMVEX///8AAADx8fHe3t77+/v4+PjV1dWAgID19fWxsbG/v785OTl4eHjGxsbLy8szMzPk5OQhISFOTk4oKCiOjo5cXFw/Pz9hYWGUlJRTU1Oenp6kpKQZGRlwcHDr6+sSEhJHR0cjp8hSAAAEIklEQVR4nO1a2ZaqMBCUVTZlUxD3///Kq+N0JyBIk3Scc89JPc6EpJJ0qjdXKwsLCwsLCwsLC4v/E34UuW4U+X/JITyu27S+3eq0XR+3f0KhiPfOAF1cfJtEVg9JPFFn3hdJuJcxDi9crl8iERymSTyxi77Bwks/s3Cc/As3k9zmWDwQm2axI5B4XsxXWZTV5RAnSXzMqsHLWZtkcewt1SWSEXhJX0cO5licevt906piLf//aIpFKC1SjQpm0UlDDKl7kBO2Kl1bbUY/pCMPp0dJR5aZYLHF6c8fWDx4lEav5Y6zbz4PFHwbfhYJTj4rkWJowk4D38Blfiw64IqbRQEzl4TQ5ormwe3kUMVJqoQ6x6zpbvM7b06KanB4yhsEhQu3h4f38W0vRgzTEoPe66I7JAO8Z039AIS/Y6UBs5JNDm4l52QRwQskR3dwi2eXkYYHAeiMjgugonPaKEx6I0+KxDnd2waOmKyKKKTk81tAg6LkL7i1ARrbxadRnA3QQBEl33RowjYKmJQcQEDMceP0sQEYHFmbwceWrHExpM8t9QOIfFhVVETl1A9gPCFWWwAML4nGAS+cObdHUSTuDqNR5igQ82SSnHswes9cqcS4h2SkeBgnXhYrFyamWAdahsPp5n8gMthZJQiwLsVfbMFExWln7tsX5UoDtThxHDN7FIUpEym9m9OmF3Rrdst4QmTIzmVyATcTo/gT6R9IK1QT8hFWElczLFZ+I9ZwdiMH4sr1yjQwRGNV9Iqf68E78HpFU3q8uBxyLfCB/S6Mgsfz9YMoPLT9KjZv8jqA5wxRVm1blW9/Nly995q3FUeQGu8hXD+0dABfae20cyx4s/hR+BvCreSJscf6QnifJ/HE3WQ7NMrmCQDM2Uc8v7gM7sjrBXfkKOqm6tosa7uqGenLmjiQ4s0096dtgaYYFNv3NjV/C3LTX+CcjYp1uB7oKbOv75tFGk/HG3G/TctqID0WZfwxKA7i0hCPHgtCi7XXPWdLH6Xoz+lIVlfs+XnIzj0jqrQv90JZQg/3prQx+SI59ENyqIvKaVtBfy7BIuCkyKIXMWr3EUTOuFyKJMnTNQ9h8goGL57YXY+FmEgpOd/pbEIgumtuB5O4VKcwifZJr1L3UaCwa4h6gM5d2dRPDMeBlpGrP3zcibp1oM/WCBvw1ZK7hUOIhrg6C2kvqqHYQf88V9LNKv4IC19ro1U8EtOoGSk6eM2yImqY2q2gq9Z0CLgdNekAd5JrJqRYq1JKsVG7tEu9cCtKCuYtbohPARvlKreLD027loa/olBRQfQGuixEx0vFRkG8lEVYAMrcKgIGofBenwaUy1SeCogfQ80ZShKpwreLf8AyDXixKvcL75XhZ7Bg7WeFb91fMBT1AphLfyoLCwsLCwsLCwsLZvwD8QUl7ccaY18AAAAASUVORK5CYII=" , style="max-height: 50px; max-width: 50px; border-radius: 25%; object-fit: cover;">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''