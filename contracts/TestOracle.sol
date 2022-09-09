// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract TestOracle is AggregatorV3Interface {

    function decimals() external view returns (uint8) {return 10;}

    function description() external view returns (string memory){return "TestOracle";}

    function version() external view returns (uint256){return 0;}

    function getRoundData(uint80 _roundId)
        external
        view
        returns (
          uint80 roundId,
          int256 answer,
          uint256 startedAt,
          uint256 updatedAt,
          uint80 answeredInRound
        ){
        return (
          10,
          156090989621,
          0,
          0,
          0
        );
    }

      function latestRoundData()
        external
        view
        returns (
          uint80 roundId,
          int256 answer,
          uint256 startedAt,
          uint256 updatedAt,
          uint80 answeredInRound
        ){return (
          10,
          156090989621,
          0,
          0,
          0
        );}
}

