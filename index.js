$(function () {
    console.log("ready!");

    async function getBalance() {
        await fetch('https://api.mybitx.com/api/1/balance', {
            // mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + btoa('h6s5ne73nfy3w:Wr6jiU_YTxupB8JSjjN30_Sc9JZg2m-N_mvCmpja32Q')
            }
        }).then(data => console.log(data));
    }
    getBalance()
});