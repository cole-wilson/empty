# Created with sailboat, the Python releaser

# v0.1.0

class empty_project < Formula
  include Language::Python::Virtualenv

  desc "empty project for sailboat testing"
  homepage "https://github.com/cole-wilson/empty"
  url "{pyhosted}" # These lines must be configured during release, not build.
  sha256 "{sha256}" # ^^^
  license "none"

  livecheck do
    url :stable
  end

  depends_on "python@3.9"



  def install
    virtualenv_install_with_resources
  end
end