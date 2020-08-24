//This divides profits between 4 team members and sends to the appropriate address

pragma solidity ^0.5.0;

// equal split
contract TeamProfitSplitter {
    // @TODO: Create four payable addresses representing `Andrew`, `Alan`, `Chris`, 'Gabe'.
    address payable Andrew;
    address payable Alan;
    address payable Chris;
    address payable Gabe;

    constructor(address payable _one, address payable _two, address payable _three, address payable _four) public {
        Andrew = _one;
        Alan = _two;
        Chris = _three;
        Gabe = _four;
    }

    function balance() public view returns(uint) {
        return address(this).balance;
    }

    function deposit() public payable {
        // @TODO: Split `msg.value` into four
        uint amount = msg.value/4; 

        // @TODO: Transfer the amount to each employee
        
        Andrew.transfer(amount);
        Alan.transfer(amount);
        Chris.transfer(amount);
        Gabe.transfer(amount);

        // @TODO: take care of a potential remainder by sending back to account (`msg.sender`)
        //uint send_to_account = msg.value - amount * 4;
        msg.sender.transfer (msg.value - amount * 4);
    }
    

    function() external payable {
        // @TODO: Enforce that the `deposit` function is called in the fallback function!
        //function deposit()
    }
}
