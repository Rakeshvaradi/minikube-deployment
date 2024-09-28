describe('frontendbackendintergration',()=>{
    it('display hello message', () =>{
        cy.visit(' http://127.0.0.1:61219/') ///Dynamic URL
        cy.contains('Hello from the Backend!')
    })
})