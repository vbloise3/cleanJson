case {1, -2, 3} do
  {1, x, 3} when x > 0 ->
    "Will match"
  _ ->
    "Would match, if guard condition were not satisfied"
end

f = fn
    x, y when x > 0 -> x + y
    x, y -> x * y
end
f.(1,3)
f.(-1,3)

cond do
   2 + 2 == 5 ->
     "This is never true"
   2 * 2 == 3 ->
     "Nor this"
   true ->
     "This is always true (equivalent to else)"
end

if nil do
   "This won't be seen"
 else
   "This will"
 end

unless false do
   "If true, this will never be seen"
end

if false, do: :this, else: :that

defmodule Math do
  def sum_list([head | tail], accumulator) do
    sum_list(tail, head + accumulator)
  end

  def sum_list([], accumulator) do
    accumulator
  end
end

IO.puts Math.sum_list([1, 2, 3], 0) #=> 6