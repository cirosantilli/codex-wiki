# Agent guidelines

This repository contains a Codex-generated knowledge written in OurBigBook markup, created with a decent amount of human guidance.

First make sure to understand how OurBigBook Markup works and use its features nicely: https://docs.ourbigbook.com

This knowledge base aims to explain things very well and to make them very interesting for humans to read. It will be published on the web.

Important guidelines:

* interlink every scientific and mathematical concept that is mentioned HEAVILY. Interlink every time it appears in an article, not just the first one
* maintain nice concept hierarchies: e.g. mathematics > calculus > fundamental theorem of calculus (don't be afraid of arbitrarily deep nodes, if it makes sense, do it). Use pieces of knowledge as wide or granular as needed. If it is a concept, create a stub at least and interlink.

  Stubs can be left empty. But if you write anything, try to interlink to existing articles and possibly create empty stubs for anything missing that shows up. You should not completely forget the task at hand and go crazy with infinite interlink depth, but equally it is worth to at least setup a nice base for a next pass when we might further improve concepts. Maybe also as you link back to something from different new locations, consider adding a little more there, as it is becoming more important.

## Exam solutions

One important activity done in this wiki is solving past undergraduate exams.

One example of this is past-exam-of-the-mathematics-course-of-the-university-of-cambridge.

There are two goals of this:

* to help future students study for future tests without reburning the tokens and the time
* to help populate our tree of important general knowledge

As such, when creating such solutions, interlink heavily as usual, and create at least stubs to every possibly reusable subject you come across. Do this even for things that seem simple like "eigenvalue". Especially for things which are not super well established, expand the stub so it will be clear what it is about. For super well established concepts, a shorter description is fine. We can expand those in a second pass when we are done solving a bunch of old exams.

Do not add model-attribution lines to solutions.

## OurBigBook primer

There are a few important ourbigbook features which you must master and use well, notably for headers:

* `{c}` for capitalization. You want to set this for every header that has a fixed capitalization
* `{disambiguate}` when something might mean something else. Feel free then to `{synonym}` to something more specific that you are using often in our STEM heavy context for example
* `{synonym}` to create different names for the same thing, in particular ones that will allow you to seamlessly `<>` interlink from other places to a given concept. You rarely want to give explicit `<id>[text]` link text, most of the time you want a synonym (or a new section) and just `<synonym-id>`. Remember that `<Dogs>` with plural and capitalization works automatically except for pluralization exceptions.
* `{wiki}` to point to wiki pages that already exist for concepts you come across. But note that not every concept header needs to have a wiki. Notably, we are much more granular than wikipedia, and don't have notability criteria: if it's cute and potentially reusable, make a header. Concepts don't even need to be just knows: we can have proper short sentences, for example stating theorems.

  Remember: we already handle simple space to underscore cases! E.g. you don't need to:

  ```
  = Chernoff bound
  {wiki=Chernoff_bound}
  ```

  just `{wiki}` would suffice here.

  Only link up to Wikipedia if it matches the exact concept of the header. E.g. this is not great:

  ```
  = Bogomolny bound
  {c}
  {parent=Quantum field theory}
  {wiki=Bogomolny_equations}
  ```

  much better would be to have an exact wiki match with either a synonym or child header:

  ```
  = Bogomolny equations
  {c}
  {parent=Quantum field theory}
  {wiki}

  = Bogomolny bound
  {c}
  {parent=Bogomolny equations}
  ```

  `{wiki}` is not a tag. It means "That wiki article is exactly about this topic".

Newlines render as `<br>`, so don't indent code, keep long lines. You almost never want a newline, unless it is followed by a block construct. This is fine though:

```
My equation:
$$
1 + 1
$$
is nice
```

as it contains a block construct. It places the block construct inside the paragraph, which is fine because OurBigBook allows for strong nesting of many constructs in general (except headers which are mroe restricted).

When in doubt, double check that the HTML output is awesome!

## STEM guidelines 

When documenting a generally useful STEM concepts, we want to aim try to have the following elements when they apply:

* what is it
* examples
* why the concept is useful and beautiful/interesting
* discovery history
* images. We are currently not handling images in this setup, but we will in the future. This raises storage and copyright challenges, but we will create guidelines in the future.

When you are doing another big job, it is OK to just create stubs for concepts without going into all this detail. But when it gets closer to the matter, this is the ideal we should strive for. To one day make the one book to rule them all.

### Mathematics guidelines

For mathematical concept headers which have a standard mathematical symbol, don't forget to title2 it.
