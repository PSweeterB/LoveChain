// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract LoveChain is ERC721Burnable, Ownable {

    address public ETHToUSDOracle;
    uint256 public feeInUSD;
    mapping (bytes32 => string) public tokenMessage;

    constructor() ERC721("LoveChain", "LCH") {
        ETHToUSDOracle = 0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419;
        feeInUSD = 10;
    }

    function setETHToUSDOracle(address _ETHToUSDOracle) public onlyOwner{
        ETHToUSDOracle = _ETHToUSDOracle;
    }

    function setFeeInUSD(uint256 _feeInUSD) public onlyOwner{
        feeInUSD = _feeInUSD;
    }

    function getFee() public view returns(uint256){
        AggregatorV3Interface priceFeed = AggregatorV3Interface(ETHToUSDOracle);
        (
            /*uint80 roundID*/,
            int price,
            /*uint startedAt*/,
            /*uint timeStamp*/,
            /*uint80 answeredInRound*/
        ) = priceFeed.latestRoundData();
        uint left = feeInUSD * (10 ** 26) % uint256(price);
        return (feeInUSD * (10 ** 26) - (left)) / (uint256(price));
    }

     function withdraw(address payable payee) public onlyOwner {
        payee.transfer(address(this).balance);
     }

    function makeLove(address to, string memory message) public payable{
        require(to != address(0), "Nobody are not able to love");
        require(msg.value >= getFee(), "There's no way, 'cause you can't pay");
        bytes32 tokenId = keccak256(abi.encodePacked(message));
        tokenMessage[tokenId] = message;
        _safeMint(to, uint(tokenId), bytes(message));
    }
}
