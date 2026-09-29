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

### OurBigBook links and references

You rarely want explicit `\a` for links because we already have implicit links:

```
Hello http://example.com site.
```

and for custom content:

```
Hello http://example.com[custom content] site.
```

Don't use explicit `\a` unless actually required.

For references, links and cross references have the `{ref}` option example:

```
The sky is blue.http://example.com{ref}
```

You must understand that this option renders as a superscript`[ref]` on HTML output, so don't count on its contents being present in the main flow of output. Therefore this is bad:

```
John Smith's https://link.springer.com/book/10.1007/978-3-540-76649-0[Using the Borsuk-Ulam Theorem, 2003]{ref} develops the theorem.
```

because it won't appear as a clearly visible part of the text, you shouldn't use `{ref}` there just:

```
Jiří Matoušek's https://link.springer.com/book/10.1007/978-3-540-76649-0[Using the Borsuk-Ulam Theorem, 2003] develops the theorem.
```

Correct usage is for `{ref}` is providing corroborating sources e.g.:

```
The sky is blue.http://mybook.com/sky[Page 22, "The sky is blue"]
```

Even though it does not show up in the direct flow of text, do use as much detail as possible on the content of a `{ref}` link when you do use  `{ref}` to say where and when reasonable quote the exact passage.

For most sources, you want to create a header for the source so that it can be reused, e.g., and then cite with `<>` e.g. the following illustrates:

```
= Climatology

The sky is blue.<Climatology 101 by John Smith>[Page 22, "The sky is blue"]

= Climatologist
{parent=Climatology}

= John Smith
{parent=Climatologist}

Homepage: https://johnsmith.com

= Work by John Smith
{parent=John Smith}

= Mary Jane
{parent=Climatologist}

Homepage: https://maryjane.com

= Work by Mary Jane
{parent=Mary Jane}

= Climatology bibliography
{parent=Climatology}

= Climatology 101 by John Smith
{parent=Climatology bibliography}
{tag=Work by John Smith}
{title2=1997}
{title2=978-0702343490}

Official website: https://climatology-101-the-book.com

Amazon: https://www.amazon.co.uk/dp/ABCDEFGHIJ

= What I like about climatology by Mary Jane
{parent=Climatology bibliography}
{tag=Work by Mary Jane}
{title2=2003}

https://maryjane.com/what-i-like-about-climatology
```

Use the "Climatology 101 by John Smith" formula when it is unambiguous enough, and add further qualification if needed e.g.:

```
= Climatology 101 by John Smith (2023)

= Climatology 101 by John Smith (2nd edition)
```

You should rarely use a non `{ref}` reference unless you are mentioning something specific about the source. Just saying stuff like:

```
See this for a good reference: <Great Book by John Smith>.
```

is depressing. We want beauty delivered here or not. What we usually want is:

```
The first mention of the word "asdfqwer" was in <Great Book by John Smith> page 12:

> I like my asdfqwer, but I prefer my qwerty.

It was then mentioned again more prominently in <Amazing Book by Mary Jane>

> What is an asdfqwer? We shall never know.
```

Or you might want to bring up specific examples or facts from such sources, paraphrasing or reusing aspects which justify fair usage such original experimental data or illustrations with historical significance. 

### OurBigBook header features

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

  Only link up to Wikipedia if it matches the exact concept of the header. E.g. this is bad:

  ```
  = Scalar multiple
  {parent=Vector space}
  {wiki=Scalar_multiplication}
  ```

  much better would be to have an exact wiki match with either a synonym or child header:

  ```
  = Scalar multiplication
  {parent=Vector space}
  {wiki}

  = Scalar multiple
  {parent=Scalar multiplication}
  ```

  `{wiki}` is not a tag. It means "That wiki article is exactly about this topic".

  Explicit `wiki=` should be used sparingly.

  When you encounter a different name for something that exists on Wikipedia, you usually want to use the Wikipedia name as the main name and a synonym to it. E.g. not great:

  ```
  = D'Alembert formula
  {wiki=D'Alembert's_formula}
  ```

  much better:

  ```
  = D'Alembert's_formula
  {wiki}

  = D'Alembert formula
  {synonym}
  ```

  but it's OK to make exceptions if the Wikipedia formatting is particularly annoying. One things that I really hate for example is Wikipedia's use of em Dash for multi-name concepts. This usage of wiki= is good therefore:

  ```
  = Radon-Riesz property
  {wiki=Radon–Riesz_property}
  ```

  It's also OK to have explicit wiki when we have a more specific version of the concept due to our focus on STEM, often Wiki uses () which we can omit, e.g. this is OK:

  ```
  = Series
  {wiki=Series_(mathematics)}
  ```

  but perhaps even better would be:

  ```
  = Series
  {disambiguate=mathematics}
  {wiki}

  = Series
  {synonym}
  ```

  Another thing to remember is that OurBigBook has strong ASCII conversions for automatic ID generation, so it is OK to keep annoying Unicode european character in people's names e.g. this is better:

  ```
  = Arzelà theorem
  ```

  than this:

  ```
  = Arzela theorem
  {wiki=Arzelà_theorem}
  ```

  because we already convert `à` -> `a` to have nice ASCII IDs where reasonable.

### Include guidelines

When using multiple `\Include`, don't add a blank line between entries. Good:

```
\Include[file1]
\Include[file2]
```

bad:

```
\Include[file1]

\Include[file2]
```

Both work but no space is nicer.

### Header guidelines

#### Header pluralization

We prefer plural form strongly unless there is specific reason not to. In particular, simple pluralized magic links seamlessly work:

```
= Dog

I like <dogs>.
```

so there's no need for:

```
= Dog

= Dogs
{synonym}

I like <dogs>.
```

This synonym makes sense when it's not the last word that is pluralized, this is good:

```
= Root of a polynomial

= Roots of a polynomial
{synonym}

I like <roots of a polynomial>.
```

## STEM guidelines 

When documenting a generally useful STEM concepts, we want to aim try to have the following elements when they apply:

* what is it
* examples
* image, maybe even video generation when it makes sense
* why the concept is useful and beautiful/interesting
* discovery history.
* in the case of the natural sciences, it is extremely important to cover motivating experiments in detail when this applies, early motivating experiments as well as simpler modern versions can both be of interest. When possible, describe even specifics of the experimental apparatus used, though this is unfortunately often lost to time.

When you are doing another big job, it is OK to just create stubs for concepts without going into all this detail. But when it gets closer to the matter, this is the ideal we should strive for. To one day make the one book to rule them all.

For now, we are STEM focused. It is OK to create stubs for any reusable non-STEM concepts, but don't expand those beyond stubs for now. You can add STEM specific aspects of non-STEM subjects, but don't steer off too far away from STEM otherwise beyond these stubs.

### Mathematics guidelines

For mathematical concept headers which have a standard mathematical symbol, don't forget to title2 it.

## Image guidelines

For now we are currently only accepting relatively small self generated images.

When you generate an image, if the image was generated via a script, keep the generator script right next to the image with same basename but different extension, e.g. my-image.py generates my-image.png. Use PNG as your preferred output format. SVG can be unreliable due to font variations, and it is less portable. Make sure not to use transparent backgrounds, normally white background unless there's reason to do otherwise.

Prefer Python for generating images, e.g. matplotlib or another Python library if something more relevant exists. Maintain a toplevel pyproject.toml documenting all dependencies and also document python version tested at. Attempt to make every script work under those versions. If one is particularly difficult, fine, create a subdirectory pyproject.toml for it.

When dealing with images be mindful of copyright. For now, we are taking a relaxed approach to this: if there's an image of something real which we cannot recreate ourselves (e.g. photos of people, photos of experimental setups, original illustrations from important papers), it is fine to use them as fair usage. However, we are not going to store them in this repo. Instead, we will link to external providers for those. The best options are Wikimedia and archive.org, but if those are not available, just use other online sources where those may be present. But for things which we can create ourselves, just create a generator script.

For every image you generate, select a reasonable image height or width, as large as needed for good viewing but not larger. There's no need to add `{height}` to the bigb for such images because we now have autodetect for such local images. It is OK to have large images on the output where needed, better have a large image that is viewable than require users to click tiny images to see them at all.

ASCII art may be acceptable in some cases, e.g. box and arrow diagrams. But don't go overboard on it, e.g. for X-Y graphs, just do an image instead generally.

When linking to images from a subdirectory, e.g. `past-exam-of-the-mathematics-course-of-the-university-of-cambridge/2018/iii/paper-316.bigb` only use the relative path to the image e.g.:
```
\Image[paper-316-rotating-frame.png]
```
not:
```
\Image[past-exam-of-the-mathematics-course-of-the-university-of-cambridge/2018/iii/paper-316-rotating-frame.png]
```

Let's have a `title=` for every Image. It is OK if it repeats the title built into the image itself when one is present.

## People guidelines

People like people. Create a dedicated article for every person that comes up. It is can be a stub, but create it. Put people under their main specialization:

```
= Mathematics

= Mathematician
{parent=Mathematics}

= List of mathematicians
{parent=Mathematician}

= John smith
{parent=List of mathematicians}
{title2=1923-}

= Mary Jane
{parent=List of mathematicians}
{title2=1911-2024}
```

Attempt to include the best bust/face image you can find of each person.

Be careful with what you say about living persons. Neutrality is particularly important there.
