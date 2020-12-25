module Philosophers where
 
import Control.Monad
import Control.Concurrent
import Control.Concurrent.STM
import System.Random
--TMVar is a transaction, it retries until successful
-- A new kind of object or "type" in Haskell, that represents the forks.
type Fork = TMVar Int
 
newFork :: Int -> IO Fork
newFork i = newTMVarIO i
 
-- Putting down and releasing forks.
takeFork :: Fork -> STM Int
takeFork fork = takeTMVar fork
 
releaseFork :: Int -> Fork -> STM ()
releaseFork i fork = putTMVar fork i

-- The names of the philosophers are represented as Strings. 
type Name = String

--runPhilosopher is a function that takes the name of a philosopher and a pair of Forks and does an action. 
runPhilosopher :: Name -> (Fork, Fork) -> IO ()
runPhilosopher name (left, right) = forever $ do
  putStrLn (name ++ " is hungry.")
 
  --Waiting for forks to be available, will not eat unless both hands have forks.
  (leftNum, rightNum) <- atomically $ do
    leftNum <- takeFork left
    rightNum <- takeFork right
    return (leftNum, rightNum)
 
  putStrLn (name ++ " got forks " ++ show leftNum ++ " and " ++ show rightNum ++ " and is now eating.")
  delay <- randomRIO (1,10)
  threadDelay (delay * 1000000) -- Delay in nanoseconds so humans can see the output
  putStrLn (name ++ " is done eating. Going back to thinking.")
 
 --When done eating the two forks that were being used are put down.
  atomically $ do
    releaseFork leftNum left
    releaseFork rightNum right
 
  delay <- randomRIO (1, 10)
  threadDelay (delay * 1000000)
 --Philosophers is an array of Strings
philosophers :: [String]
-- The Philosophers now including King Sejong the Great.
philosophers = ["Plato", "Kant", "Spinoza", "Marx", "Sejong"]
 
-- the main function starts with five forks
main = do
  forks <- mapM newFork [1..5]
  let namedPhilosophers  = map runPhilosopher philosophers
      forkPairs          = zip forks (tail . cycle $ forks)
      philosophersWithForks = zipWith ($) namedPhilosophers forkPairs
 
  putStrLn "Running the philosophers. Press enter to quit."
 
  mapM_ forkIO philosophersWithForks
   
  getLine