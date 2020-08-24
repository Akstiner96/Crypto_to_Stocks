//examples
contract MyContract {

    address alan = 0x123;
    address andrew = 
    address chris = 
    address gabe = 

    function send() {

        // send ether with default 21,000 gas
        // likely causes OOG in callee
        alan.send(1 ether);
        andrew.send(1 ether);
        chris.send(1 ether);
        gabe.send(1 ether);


        // send ether with all remaining gas
        // but no success check!
        alan.call.value(1 ether)();
        andrew.call.value(1 ether)();
        chris.call.value(1 ether)();
        gabe.call.value(1 ether)();

        // RECOMMENDED
        // send all remaining gas
        // explicitly handle callee throw
        if(!alan.call.value(1 ether)()) throw;

    }
}

pragma solidity ^0.4.18;

/**
 * Contract that will forward any incoming Ether to its creator
 */
contract Forwarder {
  // Address to which any funds sent to this contract will be forwarded
  address public destinationAddress;

  /**
   * Create the contract, and set the destination address to that of the creator
   */
  function Forwarder() public {
    destinationAddress = msg.sender;
  }

  /**
   * Default function; Gets called when Ether is deposited, and forwards it to the destination address
   */
  function() payable public {
        destinationAddress.transfer(msg.value);
  }

  /**
   * It is possible that funds were sent to this address before the contract was deployed.
   * We can flush those funds to the destination address.
   */
  function flush() public {
    destinationAddress.transfer(this.balance);
  }

}